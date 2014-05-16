import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

readFiles.extend( [
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_9_1_8rt.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_8_1_5ky.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_7_1_tpw.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_6_1_bCX.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_5_1_zMr.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_4_1_ykf.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_3_1_bpB.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_2_1_p2J.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_1_1_QZE.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_16_1_msg.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_15_1_VY9.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_14_1_2AY.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_13_1_ffX.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_12_1_mJ3.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_11_1_551.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_10_1_tVa.root'
] );

secFiles.extend( [
    ] )
