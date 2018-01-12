import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_12_1_vna.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_11_1_fwW.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_14_1_aKy.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_13_1_pi1.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_16_1_Atq.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_15_1_aZC.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_4_1_Odx.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_3_1_yDH.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_10_1_vAl.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_18_1_vCo.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_17_1_TpE.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_2_1_3sP.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_1_1_ceA.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_6_1_PLF.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_5_1_ntM.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_8_1_cWz.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_7_1_Cuh.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/pakhotin/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v1/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_9_1_kBA.root' ] );


secFiles.extend( [
               ] )