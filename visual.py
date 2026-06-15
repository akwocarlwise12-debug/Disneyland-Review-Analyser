import matplotlib.pyplot as plt

def show_chart(reviews):
    parks = {}

    for review in reviews:
        park = review["Branch"]

        if park not in parks:
            parks[park] = 0

        parks[park] += 1

    plt.pie(
        parks.values(),
        labels=parks.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Distribution of Reviews per Park")
    plt.show()

def top_10_locations_chart(reviews,park):
        location_scores = {}

        for review in reviews:
            if review["Branch"] == park:
                location = review["Reviewer_Location"]
                rating = int(review["Rating"])

                if location not in location_scores:
                    location_scores[location] = []

                location_scores[location].append(rating)

        averages = {}

        for location, ratings in location_scores.items():
            averages[location] = sum(ratings) / len(ratings)

        top_10 = sorted(
            averages.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]

        locations = [item[0] for item in top_10]
        scores = [item[1] for item in top_10]

        plt.bar(locations, scores)
        plt.title("Top 10 Reviewer Locations by Average Rating")
        plt.xlabel("Reviewer Location")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def monthly_average_chart(reviews, park):
            month_scores = {}

            for review in reviews:
                if review["Branch"] == park:
                    month = review["Year_Month"][5:7]

                    if month not in month_scores:
                        month_scores[month] = []

                    month_scores[month].append(int(review["Rating"]))

            months = []
            averages = []

            for month in sorted(month_scores.keys()):
                months.append(month)
                averages.append(sum(month_scores[month]) / len(month_scores[month]))

            plt.bar(months, averages)
            plt.title("Average Rating by Month")
            plt.xlabel("Month")
            plt.ylabel("Average Rating")
            plt.show()