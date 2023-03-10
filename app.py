import datetime
import pandas as pd
import os
import utils.extractions as extract

def output_results(data, file_name):
    output_path = 'output/' + file_name

    if os.path.exists(output_path):
        os.remove(output_path)
        data.to_excel(output_path, index=False)
    else:
        data.to_excel(output_path, index=False)


def app():
    orders = extract.read_excel('files/orders.xlsx')
    companies = extract.read_excel('files/company_data.xlsx')
    brokers = extract.read_excel('files/broker_data.xlsx')

    # Get unique codes and brokers
    stocks_info = orders[['code', 'broker']].groupby(['code', 'broker']).size().reset_index()

    # Calc total costs
    orders['total_cost'] = orders.apply(lambda x: (x['quantity'] * x['price'])* 1.003, axis=1)

    result = pd.DataFrame()
    result_descriptions = pd.DataFrame()

    # Calc average costs
    for idx, stock in stocks_info.iterrows():
        quantity = 0
        cost = 0
        avg_cost = 0
        filtered_data = orders[(orders['code'] == stock['code']) & (orders['broker'] == stock['broker'])]
        filtered_data = filtered_data.sort_values('date').reset_index()

        for idx, f in filtered_data.iterrows():
            if f['order_type'] == 'c':
                quantity += f['quantity']
                cost += f['total_cost']
            else:
                avg_cost = cost/quantity
                quantity -= f['quantity']
                cost = avg_cost * quantity

        if quantity > 0:
            new_row_avg = pd.DataFrame({
                "code": [stock['code']],
                "quantity": [quantity],
                "avg_cost": ["{:.2f}".format(cost/quantity)],
                "broker": [f['broker']]
            })

            # Write text for each stock and broker
            new_row_desc = pd.DataFrame({
                "code": [stock['code']],
                "broker": [f['broker']],
                "text": [f'{stock["code"]} - ACOES / {quantity} UNIDADES / CUSTO MEDIO R$ {str("{:.2f}".format(cost/quantity)).replace(".", ",")} / EMPRESA {companies[companies["codigo"] == stock["code"]]["empresa"].values[0]} / CUSTODIA NA CORRETORA {brokers[brokers["broker"] == stock["broker"]]["name"].values[0]} / CNPJ: {brokers[brokers["broker"] == stock["broker"]]["cnpj"].values[0]}']
            })
            
            # Output orders in excel file
            result = pd.concat([result, new_row_avg])

            # Output texts in excel file            
            result_descriptions = pd.concat([result_descriptions, new_row_desc])

    # Export results to excel
    output_results(result, 'output_avg_cost.xlsx')
    output_results(result_descriptions, 'output_descriptions.xlsx')

# TODO: Tests and data validation
# TODO: Read Nuinvest brokerages
# TODO: Read Rico brokerages
# TODO: Config variables

if __name__ == "__main__":
    app()

