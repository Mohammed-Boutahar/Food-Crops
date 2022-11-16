from FoodCropsDataset import FoodCropsDataset

datasetTest = FoodCropsDataset()

def main():
    datasetTest.load("./csv/FeedGrains.csv")

if __name__ == '__main__':
    print(main())

    a = int(input("entrez le groupe indicateur"))
    b = str(input("entrez la localisation"))
    c = int(input("entrez l'unité"))
    d = int(input("entrez la commodité"))

    FoodCropsDataset.findMeasurements(a, b, c, d)

    main()