from instamojo_wrapper import Instamojo
from digitatShop.settings import PAYMENT_API_KEY,PAYMENT_API_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Requestexite
response = api.payment_request_create(
    amount='20',
    purpose='For testing',
    send_email=True,
    email="sudhanshuraj8917@gmail.com",
    redirect_url="http://www.feelfreetocode.in"
    )

# print the long URL of the payment request.
url =  response['payment_request']['longurl']
print(url)
