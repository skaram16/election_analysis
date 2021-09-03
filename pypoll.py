{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cdf0bc76",
   "metadata": {},
   "source": [
    "The data we need to retrieve:\n",
    "1. total number of votes casted\n",
    "2. a complete list of candidates who received votes\n",
    "3. the percentage of votes each candidate won\n",
    "4. total number of votes each candidate won\n",
    "5. the winner of the election based on popular vote"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "086341d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the csv\n",
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "400fb806",
   "metadata": {},
   "outputs": [],
   "source": [
    "#assign variable for file to load and create the path\n",
    "file_to_load = os.path.join(\"Resources/election_results.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b515a3de",
   "metadata": {},
   "outputs": [],
   "source": [
    "#create filename variable to the file for direct or indirect\n",
    "file_to_save = os.path.join(\"Analysis\", \"election_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "800af324",
   "metadata": {},
   "outputs": [],
   "source": [
    "#open election results and read file\n",
    "with open(file_to_load) as election_data:\n",
    "    #read and analyze data\n",
    "    file_reader = csv.reader(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "507173cd",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/yw/vlfgkyz56gzfx_dh526r1s2m0000gn/T/ipykernel_99213/1878136046.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#print each row in CSV file\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfile_reader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "#print each row in CSV file\n",
    "for row in file_reader:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b698b37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
