def calculate(self):
        start_date_str = Entry.get(self.E1)
        start = datetime.datetime.strptime(start_date_str, '%d/%m/%Y %H:%M:%S')
        end_date_str = Entry.get(self.E2)
        end = datetime.datetime.strptime(end_date_str, '%d/%m/%Y %H:%M:%S')  
        time_elapsed = end - start
        total_hours = round(time_elapsed.total_seconds() / 3600, 2)
        self.E3.delete(0, 'end')
        Entry.insert(self.E3,0, total_hours)
        total_amount_earned = round(total_hours * 5, 2)
        self.E4.delete(0, 'end')
        Entry.insert(self.E4,0, total_amount_earned)
        with open('tracker.csv', 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile,
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([start_date_str, end_date_str, str(total_hours), str(total_amount_earned)])