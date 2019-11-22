class MuseumMoney:
    def open(self):
        file = open("C:\Users\manki\OOP-201921\MuseumsCollectionsArchives_2015.csv", "r")
        museums = []
        for line in file:
            line = line.splitlines()
            for word in line:
                if (word.istitle()):
                    pass
                else:
                    self.add(line,museums)
        file.close()

    def add(self,line,museums):
        museums.append(line)
        return museums


    def get_museum_area(self, amount):
        for index, line in enumerate(museums):
            if museums[index]

        return amount












MuseumMone=MuseumMoney()
MuseumMone.open()
MuseumMone.get_museum_area()