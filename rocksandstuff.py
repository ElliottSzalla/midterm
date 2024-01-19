#!/usr/bin/env python3
import csv
import json
import os
import sys
import random 

from operator import itemgetter

# Instructions: Locate each section with a "TODO" present, and do them!
# The program should run when you are finished. Make sure that it does.
# The dataset is meteor strikes recorded across the world.
#
# Bonus: Add a class method that will find the {count} heaviest entries,
# and output those in __main__!
# 
# NOTE: This program, as delivered, does run correctly with no errors.
# Double check that it runs for you before you start work. If it does
# not, contact me ASAP and include the error(s) that you are seeing.

class Meteorites(object):
    def __init__(self, input_file):
        if not os.path.isfile(input_file):
            raise RuntimeError(f"Unable to find the input file {input_file}. Exiting!")
        self._met_data = []
        with open(input_file, 'r', encoding='utf-8') as in_f:
            reader = csv.DictReader(in_f)
            for row in reader:
                self._met_data.append(row)
        # TODO: Sort self._met_data by id
                
        newlist = sorted(self._met_data, key=itemgetter('id')) 
        self._met_data = newlist
              
           

    # Return the total number of entries in the file.    
    @property
    def count(self):
        return len(self._met_data)

    # Return a sorted list of the years represented in the data.
    @property
    def years(self):
        all_years = set([y['year'] for y in self._met_data])
        return sorted(all_years)
    
    def meteor(self, id):
        return self._met_data[id-1]

    # Print alllll of the data (for debugging only)
    def print_all(self):
        for m in self._met_data:
            print(json.dumps(m, indent=2))

    def total_by_year(self):
        years = {}
        for m in self._met_data:
            if m['year'] not in years:
                years[m['year']] = 0
            years[m['year']] += 1
        
        # TODO: Right now, this function returns a dictionary with an
        # entry for each year and the number of landings that year, but
        # it is unsorted. This is hard to read and not all that useful.
        # The code above should be fine as-is, but your job here is to
        # SORT the dictionary before returning it.
        #
        # NOTE: There are multiple ways to do this. If you feel like
        # you would like to rewrite the code above and do it differently
        # so it is sorted from the start, feel free! 
        
        sorted_years = dict(sorted(years.items()))
        return sorted_years
        
        
        

    def _within_north_america(self, lat, lon):
        # first, convert what we got to floats, and if the conversion fails, bail out
        try: 
            lat = float(lat)
            lon = float(lon)
        except TypeError:
            return False

        # super rough boundaries:
        # lats: 10 to 70
        # longs: -150 to -60
        if (lat >= 10) and (lat <= 70) and (lon >= -150) and (lon <= -60):
            return True
        return False


    # Return a LIST of every meteor that fell in North America, sorted by
    # date, optionally returning just the {count} most recent.
    def north_america_meteors(self, count=None):
        # TODO:
        # Find every meteor that fell within the rough boundaries of 
        # North America. Sort the list by date. If {count} is not None,
        # return only the most recent {count} entries. Otherwise, return
        # the whole list.
        #
        # hints: 
        #   - LOOK AT THE DATA FIRST. You need to understand what is there
        #     before you can figure out how to sort/filter it. Look at the
        #     CSV but also print out the data from within the program here.
        #     I even wrote a function that will do that for you! Add it
        #     temporarily at the bottom in the __main__ section to see the
        #     output. Remember to remove this after you are done.
        #   - I already provided a function that will check a latitude and 
        #     longitude pair to see if it falls within the rough boundaries
        #     of North America. Use that to make your life easier.
        #   - Look closely at the function args. We use an optional 
        #     "count" argument that defaults to None. Make sure that you handle
        #     other values correctly and don't ignore this argument! If it is
        #     None, you should return ALL values.
        #   - Don't forget to make sure that your list is sorted by year
        #     before returning it!
        meteors = []
        return meteors

    # Return a LIST of the years with the MOST entries, sorted by number of entries
    def top_years(self, count=5):
        # TODO:
        # Find the {count} top years with the most entries. This should be easy
        # to do because there is already a function to return hits by year, and
        # you already have to TODO to sort that list. Do that first and then do
        # this one!
        years = {}
        for m in self._met_data:
            if m['year'] not in years:
                years[m['year']] = 0
            years[m['year']] += 1

        sorted_years = sorted(years.items(), key=lambda x: x[1], reverse=True)
        top_years = sorted_years[count]
        return top_years
    
    # Return one or {count} RANDOM entry/ies from the list of meteorites!
    def pick_random(self, count=1):
        # TODO:
        # Use the Python random library to pick {count} random values for IDs,
        # then return those entries. Hint: There's already a meteor() method
        # that will pull the data for a given ID, but only AFTER the list is 
        # sorted! You have a TODO for that at the top of the file. Do that
        # before you try to do this.
        
          
        meteor_id = meteor(self, count)
        random_id = random.sample(meteor_id, count)
        randoms = [meteor(id) for id in random_id]
        return randoms

# main
if __name__ == "__main__":
    input_file = "Meteorite_Landings.csv"

    mets = Meteorites(input_file)
    print(mets.count)

    totals = mets.total_by_year()
    for y in totals.keys():
        print(f"{y}: {totals[y]}")

    #m = mets.meteor(3)
    #print(mets.within_north_america(m['reclat'], m['reclong']))

    # TODO: Change the code below to print the data from your function
    #       calls NICELY, like a human would want to read it. You'll probably
    #       want to do something like using a for loop with the data so that
    #       you can format each line nicely. 
    print(mets.north_america_meteors())
    print(mets.top_years(count=5))
    print(mets.pick_random(count=5))