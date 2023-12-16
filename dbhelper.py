import mysql.connector

class DB:
    def __init__(self):
        # connect to database
        try:
            self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='flights')

            self.mycorsor = self.conn.cursor()
            print("Connection Established")
        except:
            print('Connection Error')

    def fetch_source_city_name(self):
        source_city = []
        self.mycorsor.execute("SELECT DISTINCT(Source) FROM flights.flights")
        data = self.mycorsor.fetchall()
        for city in data:
            source_city.append(city[0])
        return source_city

    def fetch_destination_city_names(self):

        destination_city = []
        self.mycorsor.execute("SELECT DISTINCT(Destination) FROM flights.flights")

        data = self.mycorsor.fetchall()
        for item in data:
            destination_city.append(item[0])

        return destination_city

    def fetch_all_flights(self,source,destination):

        self.mycorsor.execute("""
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycorsor.fetchall()
        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []
        self.mycorsor.execute("""
        SELECT Airline,COUNT(*) AS 'frequency' FROM flights
        GROUP BY Airline
        """)

        data = self.mycorsor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.mycorsor.execute("""
        SELECT Source, COUNT(*) FROM (SELECT Source FROM flights
        UNION ALL
        SELECT Destination FROM flights) t
        GROUP BY t.Source
        """)

        data = self.mycorsor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def fetch_daily_flights(self):

        date = []
        count = []

        self.mycorsor.execute("""
        SELECT Date_of_Journey, COUNT(*) FROM flights
        GROUP BY Date_of_Journey
        ORDER By Date_of_Journey
        """)

        data = self.mycorsor.fetchall()
        for item in data:
            date.append(item[0])
            count.append(item[1])

        return date, count

    def flights_between_cities(self):

        count1 = []
        cities = []
        self.mycorsor.execute("""
        SELECT *, CONCAT(Source,'-', Destination) AS two_city 
        FROM (SELECT Source, Destination, COUNT(*) FROM flights
        GROUP BY Source, Destination) t
        """)

        data = self.mycorsor.fetchall()

        for item in data:
            count1.append(item[2])
            cities.append(item[3])

        return count1, cities

    def fetch_avg_price(self):
        Airline = []
        price = []
        self.mycorsor.execute("""
        SELECT Airline, ROUND(AVG(Price),1) AS 'avg_price'
        FROM flights
        GROUP BY Airline
        """)
        data = self.mycorsor.fetchall()

        for item in data:
            Airline.append(item[0])
            price.append(item[1])

        return Airline, price
