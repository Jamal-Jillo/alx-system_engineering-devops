#!/usr/bin/env ruby
#phone number with no space before, after, in between or no other characters
#^start of digit, $end of digit

puts ARGV[0].scan(/^\d{,10}$/).join
