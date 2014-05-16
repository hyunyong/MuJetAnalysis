import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

readFiles.extend( [
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_9_1_3Cm.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_8_1_0wM.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_7_1_c9M.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_6_1_C2B.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_5_1_g60.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_4_1_0f7.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_3_1_sIG.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_2_1_Yom.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_1_2_ipp.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_15_1_ayf.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_14_1_k6S.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_13_1_cWI.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_12_1_BpG.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_11_1_pIG.root',
       '/store/user/pakhotin/data/MC_8TeV/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/pakhotin/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1/d7ec853f1412ed77b3135ca95d8b3a46/output_10_1_oKc.root'
] );

secFiles.extend( [
    ] )
