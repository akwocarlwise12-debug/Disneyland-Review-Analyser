
from process import (
    load_data,
    get_reviews_by_park,
    count_reviews_by_location,
    average_rating_by_year,
    average_rating_by_location,
    create_export_summary
)
from visual import show_chart, top_10_locations_chart, monthly_average_chart
from exporter import TXTExporter, CSVExporter, JSONExporter
title = "Disneyland Review Analyser"
print("-" * len(title))
print(title)
print("-" * len(title))

reviews = load_data()

print("\nDataset loaded successfully.")
print("Number of rows:", len(reviews))

while True:
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")

    choice = input("\nEnter your choice: ").upper()

    if choice == "A":
        print("\n[A] View Reviews By Park")
        print("[B] Count Reviews By Location")
        print("[C] Average Rating By Park And Year")
        print("[D] Average Rating By Reviewer Location")

        sub_choice = input("\nEnter your choice: ").upper()

        if sub_choice == "A":
            park = input("Enter park name: ")
            park_reviews = get_reviews_by_park(reviews, park)
            for review in park_reviews[:10]:
                print(review)

        elif sub_choice == "B":
            park = input("Enter park name: ")
            location = input("Enter reviewer location: ")
            total = count_reviews_by_location(reviews, park, location)
            print("\nReviews found:", total)

        elif sub_choice == "C":
            park = input("Enter park name: ")
            year = input("Enter year: ")
            average = average_rating_by_year(reviews, park, year)
            print("\nAverage rating:", average)

        elif sub_choice == "D":
            location = input("Enter reviewer location: ")
            averages = average_rating_by_location(reviews, location)

            print("\nAverage rating by park for", location)
            for park, average in averages.items():
                print(park, ":", average)

    elif choice == "B":
        print("\n[A] Most Reviewed Parks")
        print("[B] Top 10 Locations By Rating")
        print("[C] Average Rating By Month")

        sub_choice = input("\nEnter your choice: ").upper()

        if sub_choice == "A":
            show_chart(reviews)

        elif sub_choice == "B":
            park = input("Enter park name: ")
            top_10_locations_chart(reviews, park)

        elif sub_choice == "C":
            park = input("Enter park name: ")
            monthly_average_chart(reviews, park)
            print("[A] View Data")
            print("[B] Visualise Data")
            print("[C] Export Data")
            print("[X] Exit")
    elif choice == "C":
        export_data = create_export_summary(reviews)

        print("\nChoose export format:")
        print("[A] TXT")
        print("[B] CSV")
        print("[C] JSON")

        export_choice = input("\nEnter your choice: ").upper()

        if export_choice == "A":
            exporter = TXTExporter()
            exporter.export(export_data, "disneyland_export.txt")
            print("TXT file exported.")

        elif export_choice == "B":
            exporter = CSVExporter()
            exporter.export(export_data, "disneyland_export.csv")
            print("CSV file exported.")

        elif export_choice == "C":
            exporter = JSONExporter()
            exporter.export(export_data, "disneyland_export.json")
            print("JSON file exported.")

        else:
            print("Invalid export choice.")
    elif choice == "X":
        print("You have chosen option X - Exit")
        break

    else:
        print("Invalid choice. Please try again.")