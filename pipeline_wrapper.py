#!/usr/bin/python

############################################################
##################### Cancer Pipeline ######################
######## Authors: Michael A. Gonzalez and Matt Field #######
##################### Date: 2014-09-10 #####################
############################################################


import sys, re, os, subprocess, math, collections, argparse, time
from subprocess import Popen, PIPE
import pipeline_utilities


## Pass arguments Make sure to add how to open samples clinical data and map the familyID, sex, affection status.
parser = argparse.ArgumentParser(description='This is Cancer pipeline wrapper script')
parser.add_argument('-P', '--pipeline_type', dest='pipeline_type', action='store', required=True, help='Which pipeine to run', choices=['MuTect', 'VarScan2', 'Full'])
parser.add_argument('-N', '--normal_bam', dest='normal_bam', action='store', required=True, help='File with list of normal bam files')
parser.add_argument('-T', '--tumor_bam', dest='tumor_bam', action='store', required=True, help='File with list of tumor bam files')
parser.add_argument('-D', '--output_path', dest='output_path', action='store', required=True, help='Full path to store all output')
parser.add_argument('-O', '--output_prefix', dest='output_prefix', action='store', required=True, help='All output files should start with this prefix')
parser.add_argument('-V', '--version', action='version', version="%(prog)s version 0.0.1")

## Grab command line flags
args = vars(parser.parse_args())

print 'Initializing the Cancer Pipeline.... Will run the {0} version\n\n'.format(args['pipeline_type'])

## This will build the commands needed to run MuTect pipeline
if args['pipeline_type'] in ['MuTect','Full']:
	MuTect_cmd = pipeline_utilities.runMuTect(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for MuTect: {0}\n\n'.format(MuTect_cmd['job'])
	
	reformat_for_Oncotator_cmd = pipeline_utilities.prepareForOncotator('MuTect',args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for reformatting MuTect Output: {0}\n\n'.format(reformat_for_Oncotator_cmd['job'])
	
	Oncotator_cmd = pipeline_utilities.runOncotator(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for Oncotator: {0}\n\n'.format(Oncotator_cmd['job'])
	
	reformat_for_MutSigCV_cmd = pipeline_utilities.prepareForMutSigCV(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for reformatting Oncotator Output for MutSigCV: {0}\n\n'.format(reformat_for_MutSigCV_cmd['job'])
	
	MutSigCV_cmd = pipeline_utilities.runMutSigCV(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for running MutSigCV on MuTect output: {0}\n\n'.format(MutSigCV_cmd['job'])
	

## This will build the commands needed to run VarScan2 pipeline
if args['pipeline_type'] in ['VarScan2','Full']:
	Samtools_cmd = pipeline_utilities.runSamTools(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for SamTools mpileup: {0}\n\n'.format(Samtools_cmd['job'])
	
	VarScan2_cmd = pipeline_utilities.runVarScan2(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for VarScan2: {0}\n\n'.format(VarScan2_cmd['job'])
	
	reformat_for_Oncotator_cmd = pipeline_utilities.prepareForOncotator('VarScan2',args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for reformatting VarScan2 Output: {0}\n\n'.format(reformat_for_Oncotator_cmd['job'])
	
	Oncotator_cmd = pipeline_utilities.runOncotator(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for Oncotator: {0}\n\n'.format(Oncotator_cmd['job'])
	
	reformat_for_MutSigCV = pipeline_utilities.prepareForMutSigCV(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for reformatting Oncotator Output for MutSigCV: {0}\n\n'.format(reformat_for_MutSigCV['job'])
	
	MutSigCV_cmd = pipeline_utilities.runMutSigCV(args['normal_bam'],args['tumor_bam'],args['output_path'],args['output_prefix'])
	print 'Submitted job for reformatting Oncotator Output for MutSigCV: {0}\n\n'.format(MutSigCV_cmd['job'])


