import csv
import json


class Exporter:
    def export(self, data, filename):
        pass


class TXTExporter(Exporter):
    def export(self, data, filename):
        with open(filename, "w") as file:
            for park, summary in data.items():
                file.write(f"Park: {park}\n")
                file.write(f"Number of reviews: {summary['number_of_reviews']}\n")
                file.write(f"Positive reviews: {summary['positive_reviews']}\n")
                file.write(f"Average rating: {summary['average_rating']}\n")
                file.write(f"Countries reviewed: {summary['countries_reviewed']}\n")
                file.write("-" * 40 + "\n")


class CSVExporter(Exporter):
    def export(self, data, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Park",
                "Number of Reviews",
                "Positive Reviews",
                "Average Rating",
                "Countries Reviewed"
            ])

            for park, summary in data.items():
                writer.writerow([
                    park,
                    summary["number_of_reviews"],
                    summary["positive_reviews"],
                    summary["average_rating"],
                    summary["countries_reviewed"]
                ])


class JSONExporter(Exporter):
    def export(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)