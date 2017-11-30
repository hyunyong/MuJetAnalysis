import FWCore.ParameterSet.Config as cms

cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer_MiniAOD',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    muJetOrphans = cms.InputTag("PFMuJetProducer05", "Orphans"),
    tracks = cms.InputTag("unpackedTracksAndVertices"),
    TriggerResults = cms.InputTag("TriggerResults","","HLT"),
    TrackRefitter = cms.InputTag("TrackRefitter"),
    genParticles = cms.InputTag("prunedGenParticles"),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(0),
    barrelPixelLayer = cms.int32(1),
    endcapPixelLayer = cms.int32(1),
    runDisplacedVtxFinder = cms.bool(False),
    Traj = cms.InputTag("TrackRefitter"),
    NavigationSchool   = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    Propagator = cms.string("RungeKuttaTrackerPropagator"),
    runBBestimation = cms.bool(True),
    skimOutput = cms.bool(False),
    ## no need to version it!
    signalHltPaths = cms.vstring(
        'HLT_TrkMu16_DoubleTrkMu6NoFiltersNoVtx',
    ),
)