# Stocks Income Tax
This repository aims to help people calculate the average costs of their stocks to declare in the income tax.


## Getting started
The application will read your stock market orders using an Excel file or your brokerage notes.

### Brokerages method
Download the brokerages and move the files to the `orders` folder. So far, the app supports these brokerage notes:
* :construction_worker: In progress - Nuinvest
* :construction_worker: In progress - Rico Investimentos


### Excel file method
On the `files` folder, fill the excel file `orders.xlsx` inserting each share of all your orders. The file already have some examples to you follow.
#### Columns:
* date: When the order was made using the format "dd/mm/yyyy".
* order_type: Buy or sell (c/v)
* code: Share id in stock market.
* quantity: Quantity bought/selled of the share.
* price: Price payed at the bought/selled moment.
* broker: Broker identifier (see the column `broker` on file `broker_data.xlsx` for options).


## :computer: Setting up environment
1 - [Install python](https://www.python.org/downloads/).

2 - Clone the repository:
`git clone https://github.com/ecmatos/stock_income_tax.git`

3 - Go to the folder where you cloned the repository.

4 - Create a new virtual environment:
`python -m venv venv`

5 - Activate the virtual environment:
`venv\Scripts\activate.bat`

6 - Install the dependencies listed on requirements.txt:
`pip install -r requirements.txt`


## :computer: Running the app
Runnig the app
* `python app.py`

## :mag_right: Resources
The folder `files` have some other excel files that you can explore:
* `broker_data.xlsx` store information about brokers, so if you didn't find your broker on the list, you can add it on the file using the other rows as example.
* `company_data.xlsx` contain all the brazilian companies listed in the stock market.

## :page_facing_up: Consuming the results
The app will create 2 files as result on `output` folder:
* output_avg_cost.xlsx : This file contains all information summarized in share code, quantity and average cost.
* output_descriptions.xlsx : This file contains the standard texts that can be used in the income tax.

## :hammer: Built with
* Pandas
* PyPDF2