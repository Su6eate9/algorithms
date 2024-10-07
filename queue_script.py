from collections import deque  # Make sure this is at the top of your script

class BancoQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, customer):
        self.queue.append(customer)
        print(f"Customer {customer} added to the queue.")

    def serve_customer(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"Serving customer {customer}.")
        else:
            print("No customers in the queue to serve.")

    def queue_size(self):
        return len(self.queue)

    def next_customer(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

# Example usage
bank_queue = BancoQueue()

# Adding customers to the queue
bank_queue.add_customer("Ana")
bank_queue.add_customer("Clarice")
bank_queue.add_customer("Atlas")

# Serving customers
bank_queue.serve_customer()
bank_queue.serve_customer()

# Checking the next customer
next_customer = bank_queue.next_customer()
if next_customer:
    print(f"The next customer to be served is: {next_customer}")
else:
    print("There are no more customers in the queue.")

# Checking the current queue size
print(f"Current queue size: {bank_queue.queue_size()}")

# Serving the rest of the customers
bank_queue.serve_customer()
bank_queue.serve_customer()
