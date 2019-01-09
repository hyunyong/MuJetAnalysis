#!/bin/bash

if [ ! -d  SBATCH_JOBS_RECOAOD ];then
    mkdir SBATCH_JOBS_RECOAOD
fi;

if [ ! -d  SBATCHLOG_RECOAOD ];then
    mkdir SBATCHLOG_RECOAOD
fi;


while read line
do
name=$line
echo "Sample - $name"

echo " name folder   "  $name
     
mkdir $name
      
#nJobs=$(wc -l python/$name.txt | cut -f1 -d' ')
nJobs=100
      
echo "Number of Jobs   $nJobs"
   
cat  >  SBATCH_JOBS_RECOAOD/${name}.slrm <<EOF
#!/bin/bash      
#SBATCH -J AnaMiniAOD
#SBATCH -n1
#SBATCH --time=08:30:00
#SBATCH --mem-per-cpu=8000mb
#SBATCH -p stakeholder
#SBATCH --array=1-$nJobs
#SBATCH -o $PWD/SBATCHLOG_RECOAOD/SBATCH_%a.stdout
#SBATCH -e $PWD/SBATCHLOG_RECOAOD/SBATCH_%a.stderr
      
export PROCESS=\$SLURM_ARRAY_TASK_ID
cd /fdata/scratch/castaned/DisplacedMuonJetAnalysis_2016/CMSSW_8_0_20/src
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc493
eval \`scramv1 runtime -sh\`
cd /fdata/scratch/castaned/DisplacedMuonJetAnalysis_2016/CMSSW_8_0_20/src/MuJetAnalysis/CutFlowAnalyzer/test
cmsRun patTuple_cutana_mujets_73X_cfg.py  $name $nJobs
      
exit 0

EOF
done < $1

