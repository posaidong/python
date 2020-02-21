import csv
import time

import Util.GoogleTranslate


def translateReviewsToEnglish(csvFile, outFile):
    file = open(csvFile, encoding='utf16')
    line = file.readline()

    out = open(outFile, 'w', encoding='utf16')
    out.write('App Version Name,Device,Star Rating,Review Text\n')

    i = 0

    csvReader = csv.reader(file)
    for row in csvReader:
        i = i + 1

        # if i > 3:
        #     break

        appVersion = row[2]
        language = row[3]  # en or zh-Hans or zh-Hant
        device = row[4]
        starRating = row[9]
        reviewTitle = row[10]  # always empty
        reviewText = row[11]
        reviewTextEn = ''

        if reviewText:
            retryTimes = 0

            if language in ['en', 'zh-Hans', 'zh-Hant']:
                reviewTextEn = reviewText
            else:
                while True:
                    time.sleep(10)  # google will block access if call its api too frequently
                    isSuccess, reviewTextEn = Util.GoogleTranslate.translate(reviewText)
                    retryTimes += 1
                    if isSuccess or retryTimes > 3:
                        break

        print(str(i) + ':   ' + appVersion + ',' + starRating + ',' + reviewTextEn)

        out.write(appVersion + ',' + device + ',' + starRating + ',' + reviewTextEn.replace(',', '.') + '\n')

    out.close()
    file.close()


def main():
    csv = 'ds/reviews_reviews_com.harman.ble.jbllink_202001.csv'
    outFile = 'ds/en.csv'
    translateReviewsToEnglish(csv, outFile)


if __name__ == '__main__':
    main()
