import csv

def load_data():
    reviews = []

    with open("disneyland_reviews.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            reviews.append(row)

    return reviews

def get_reviews_by_park(reviews, park):
    matching_reviews = []

    for review in reviews:
        if review["Branch"] == park:
            matching_reviews.append(review)

    return matching_reviews


def count_reviews_by_location(reviews, park, location):

    count = 0

    for review in reviews:

        if (
            review["Branch"] == park and
            review["Reviewer_Location"] == location
        ):
            count += 1

    return count


def average_rating_by_year(reviews, park, year):
    total = 0
    count = 0

    for review in reviews:
        if review["Branch"] == park and review["Year_Month"].startswith(year):
            total += int(review["Rating"])
            count += 1

    if count == 0:
        return 0

    return round(total / count, 2)

def average_rating_by_location(reviews, location):
    park_scores = {}

    for review in reviews:
        if review["Reviewer_Location"] == location:
            park = review["Branch"]
            rating = int(review["Rating"])

            if park not in park_scores:
                park_scores[park] = []

            park_scores[park].append(rating)

    averages = {}

    for park, ratings in park_scores.items():
        averages[park] = round(sum(ratings) / len(ratings), 2)

    return averages


def create_export_summary(reviews):
    summary = {}

    for review in reviews:
        park = review["Branch"]
        rating = int(review["Rating"])
        location = review["Reviewer_Location"]

        if park not in summary:
            summary[park] = {
                "number_of_reviews": 0,
                "positive_reviews": 0,
                "total_rating": 0,
                "countries": set()
            }

        summary[park]["number_of_reviews"] += 1
        summary[park]["total_rating"] += rating
        summary[park]["countries"].add(location)

        if rating >= 4:
            summary[park]["positive_reviews"] += 1

    for park in summary:
        total = summary[park]["number_of_reviews"]
        summary[park]["average_rating"] = round(summary[park]["total_rating"] / total, 2)
        summary[park]["countries_reviewed"] = len(summary[park]["countries"])

        del summary[park]["total_rating"]
        del summary[park]["countries"]

    return summary