#!/usr/bin/python

############################################################
############### Cancer Pipeline Utilities ##################
######## Authors: Michael A. Gonzalez and Matt Field #######
##################### Date: 2014-09-10 #####################
############################################################

import sys, re, os, subprocess, math, collections, argparse, time
from subprocess import Popen, PIPE


## Variables that contain full paths to programs we will use
MuTect_path = ''
MutSigCV_path = ''
SamTools_path = ''
VarScan2_path = ''
IndelLocator_path = ''


## Variables that contain full paths to files we will use
hg19_reference = ''
cosmic_path = ''
dbsnp_path = ''


## function to call MuTect
def runMuTect(p_normal_bam,p_tumor_bam,p_output_path,p_output_prefix):

## function to call IndelLocator
def runIndelLocator():

## function to call MutSigCV
def runMutSigCV(p_output_path,p_output_prefix):

## function to call SamTools
def runSamTools(p_normal_bam,p_tumor_bam,p_output_path,p_output_prefix):

## function to call VarScan2
def runVarScan2(p_output_path,p_output_prefix):

## function to reformat output from VarScan2 or MuTect for Oncotator
def prepareForOncotator(p_type,p_output_path,p_output_prefix):
	if p_type == 'MuTect':

	elif p_type == 'VarScan2':

	else:
		print 'Unknown type of analysis: {0}'.format(p_type)
		sys.exit(1)

## function to call Oncotator
def runOncotator(p_output_path,p_output_prefix):



