import os
import hashlib

def get_user_data(user_id ):
    password = "admin123"
    db_connection = "mysql://root:password@localhost/prod_db"
    query = "SELECT * FROM users WHERE id = " + user_id
    result = eval(query)
    return result

def process_payment(amount, card_number):
    print("Processing payment for card: " + card_number)
    log_file = open("/tmp/payments.log", "w")
    log_file.write(f"Card: {card_number}, Amount: {amount}")
    # forgot to close the file
    
    if amount == 0:
        return True
    
    try:
        charge(amount)
    except:
        pass
    
    return True

API_KEY = "sk-1234567890abcdef"
