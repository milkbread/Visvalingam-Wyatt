#!/usr/bin/env python
import getopt
import sys

def getIOFiles(): 
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	
	#print 'Input file is ', inputfile, len(inputfile)
	#print 'Output file is ', outputfile, len(outputfile)

	if(len(inputfile)==0 or len(outputfile)==0):
		print 'You have to define in- and outputfile!!!'
		sys.exit()
	else:
		return inputfile, outputfile;	

def getIOFilesRoute(): 
	outputfile = ''
	startcoord = ''
	endcoord = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"ho:s:e:",["ofile=","start=","end="])
	except getopt.GetoptError:
		print 'test.py -o <outputfile> -s <start> -e <end>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -o <outputfile> -s <start> -e <end>'
			print 'Offer coordinates in that form: <latitude, longitude>'
			sys.exit()
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-s", "--start"):
			startcoord = arg
		elif opt in ("-e", "--end"):
			endcoord = arg
	
	#print 'Input file is ', inputfile, len(inputfile)
	#print 'Output file is ', outputfile, len(outputfile)

	if(len(outputfile)==0 or len(startcoord)==0 or len(endcoord)==0):
		print 'You have to define outputfile and the coordinates of start- & endpoints <latitude, longitude>!!!'
		sys.exit()
	else:
		return outputfile, startcoord, endcoord;	

def getIOFilesThreshold(): 
	inputfile = ''
	outputfile = ''
	threshold = '0.1';
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:t:",["ifile=","ofile=", "threshold="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile> -t <threshold>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile -t <threshold>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-t", "--threshold"):
			threshold = arg

	#print 'Input file is ', inputfile, len(inputfile)
	#print 'Output file is ', outputfile, len(outputfile)

	if(len(inputfile)==0 or len(outputfile)==0):
		print 'You have to define in- and outputfile!!!'
		sys.exit()
	else:
		print 'Threshold = ', threshold
		return inputfile, outputfile, threshold;	