# Secret Santa

A simple script to assign a group of people to unique recipients and text them their assignment. 

## Requirements

A (non-included) `keys.py` file with the following items.

```python
# Sample _keys.py file
people = {
    "Person1": '14250000000', # phone number
    "Person2": '12060000000',
    "Person3": '16170000000',
    "Person4": '14280000000'
}

# Nexmo
nexmo_api_key = 'nexmokey'
nexmo_api_secret = 'nexmosecretkey'
nexmo_sender = 'nexmo_registered_sender_number'
```

## Usage

Create a `_keys.py` file like above and then execute `main.py` with all package requirements installed `pip install -r requirements.txt`. That's all.