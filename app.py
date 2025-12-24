# Bangalore Traffic Time Estimator using Kiro custom context

def traffic_estimator(source, destination, time):
    # Read local context from product.md
    with open(".kiro/product.md", "r", encoding="utf-8") as file:
        local_context = file.read()

    print("🚦 Bangalore Traffic Time Estimator")
    print("----------------------------------")
    print(f"From       : {source}")
    print(f"To         : {destination}")
    print(f"Travel Time: {time}")
    print()

    # Simple traffic estimation logic
    if time in ["8 AM", "9 AM", "10 AM", "6 PM", "7 PM", "8 PM"]:
        estimate = "High traffic expected: 2 to 2.5 hours"
    else:
        estimate = "Moderate traffic expected: 1 to 1.25 hours"

    print("⏱ Estimated Travel Time")
    print(estimate)

    print("\n📘 Local Context Used (from product.md):")
    print("---------------------------------------")
    print(local_context)


# Example run
traffic_estimator("Whitefield", "Electronic City", "9 AM")

