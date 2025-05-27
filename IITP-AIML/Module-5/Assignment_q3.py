# Program to calculate Cost Per Lead (CPL)

def calculate_cpl(clv, cm, num_conversions, num_leads):
    cpa  = clv * cm
    conversion_rate = num_conversions / num_leads
    cpl = cpa * conversion_rate
    return cpl, cpa

# Example usage:
clv = float(input("Enter Customer Lifetime Value (CLV): "))
cm = float(input("Enter Contribution Margin (as decimal, e.g., 0.25 for 25%): "))
num_conversions = int(input("Enter Number of Conversions: "))
num_leads = int(input("Enter Number of Leads: "))

cpl, cpa = calculate_cpl(clv, cm, num_conversions, num_leads)
print(f"Cost Per Acquisition (CPA): Rs {cpa:.2f}")
print(f"Cost Per Lead (CPL): Rs {cpl:.2f}")
