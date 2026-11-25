
# Hospital Billing and Patient Classification

patients = []
bills = []

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    # Validate billing constraints
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges! Charges cannot be negative.")
        continue

    total = consultation + diagnostic + treatment

    # Apply concession
    if total >= 10000:
        concession = total * 0.15
    elif total >= 5000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    # Payment details
    paid = float(input("Enter amount paid: "))

    if paid < 0:
        print("Invalid payment amount.")
        continue

    if paid > final_bill:
        print("Payment exceeds the final bill.")
        continue

    balance = final_bill - paid

    # Patient classification
    if balance == 0:
        status = "Fully Paid"
    elif paid > 0:
        status = "Partially Paid"
    else:
        status = "Unpaid"

    patients.append(name)
    bills.append(final_bill)

    print("\n--- Patient Bill ---")
    print("Patient Name:", name)
    print("Total Charges:", round(total, 2))
    print("Concession:", round(concession, 2))
    print("Final Bill:", round(final_bill, 2))
    print("Amount Paid:", round(paid, 2))
    print("Balance:", round(balance, 2))
    print("Patient Classification:", status)

# Display all patient bills
print("\n--- Hospital Billing Summary ---")

for i in range(len(patients)):
    print(patients[i], ":", round(bills[i], 2))

print("\nHospital Billing Completed.")
