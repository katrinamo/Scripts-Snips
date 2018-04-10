# Scripts-Snips
Snippets of code and scripts to make life easier.

##Bash-Blast
Current files:
    1. .bashrc 
    2. frequecy_counter.sh 

###.bashrc
A (currently) small bash rc fle with a quality of life alias.

###frequecy_counter.sh
USAGE: ./frequency_counter.sh [FILENAME] [*options*]

This script will separate the provided file into individual words. Word
initial and word final punctuation is truncated. Word medial
punctuation is not touched. Additionally, all words are put into lower
case. The number of occurrences of each word is counted and displayed
with number of occurences, sorted from those that appear most to those
that appear least.

OPTIONS:

    --expand
    
    This option keeps all intermediate files for debugging. These
    include a file of the tokens separated by newlines and the cleaned
    tokens sepearated by newlines.
