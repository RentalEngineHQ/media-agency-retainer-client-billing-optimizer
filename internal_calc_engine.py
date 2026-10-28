# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(active_hours, contract_hours, hourly_rate):
    overage_hours = max(0.0, float(active_hours) - float(contract_hours))
    overage_revenue = overage_hours * float(hourly_rate)
    return overage_hours, overage_revenue
