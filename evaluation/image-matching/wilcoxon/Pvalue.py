from scipy.stats import wilcoxon

# Assuming you have a list of difference scores
accuracy_diff = [0.4152910209
,0.4152910209
,0.4784376785
,0.4784376785
,0.4453911574
,0.4453911574
,0.4281561739
,0.4152910209
,0.4784376785
,0.4753091857
,0.4152910209
,0.4830097137
,0.4830097137
,0.4784376785
,0.4453911574
,0.4830097137
,0.4588881757
,0.4897720094
,0.4509932067
,0.4703770115
,0.4784376785
,0.4509932067
,0.4784376785
,0.4509932067
,0.4588881757
,0.4830097137
,0.4784376785
,0.4830097137
,0.4830097137
,0.4830097137
,0.4897720094
,0.4830097137
,0.4703770115
,0.4830097137
,0.4509932067
,0.4830097137
,0.4509932067
,0.4897720094
,0.4897720094
,0.4897720094
,0.4897720094
,0.4897720094
,0.3489960851
,0.4281561739
,0.4703770115
,0.4281561739
,0.4281561739
,0.3833737441
,0.4588881757
,0.4897720094
,0.4151735045
,0.3833737441
,0.4703770115
,0.4830097137
,0.4588881757
,0.4703770115
,0.4784376785
,0.3630224959
,0.4061625393
,0.3833737441
,0.2491726853
,0.4281561739
,0.4784376785
,0.4588881757
,0.4152910209
,0.4152910209
,0.4509932067
,0.4588881757
,0.4784376785
,0.4588881757
,0.4753091857
,0.4897720094
,0.4509932067
,0.4830097137
,0.5
,0.4588881757
,0.4897720094
,0.4830097137
,0.4588881757
,0.4152910209
,0.4509932067
,0.4897720094
,0.4588881757
,0.4830097137
,0.3489960851
,0.4588881757
,0.4784376785
,0.4281561739
,0.4061625393
,0.4453911574
,0.4061625393
,0.4703770115
,0.3833737441
,0.4281561739
,0.4588881757
,0.4830097137
,0.4703770115
,0.5
,0.4784376785
,0.4897720094
,0.4753091857
,0.4453911574
,0.4830097137
,0.4830097137
,0.4830097137
,0.4509932067
,0.4784376785
,0.4703770115
,0.4281561739
,0.4588881757
,0.4784376785
,0.4472006344
,0.4588881757
,0.3833737441
,0.4703770115
,0.4703770115
,0.4830097137
,0.4784376785
,0.4897720094
,0.4152910209
,0.4897720094
,0.4703770115
,0.487845443
,0.4784376785
,0.4152910209
,0.4830097137
,0.4281561739
,0.4281561739
,0.3630224959
,0.3630224959
,0.4897720094
,0.4453911574
,0.4703770115
,0.4784376785
,0.4703770115
,0.4703770115
,0.4784376785
,0.4897720094
,0.4588881757
,0.4897720094
,0.4830097137
,0.3489960851
,0.4152910209
,0.4830097137
,0.4509932067
,0.4830097137
,0.4897720094
,0.4830097137
,0.4509932067
,0.4281561739
,0.4703770115
,0.3630224959
,0.4830097137
,0.2683830901
,0.4509932067
,0.4281561739
,0.3489960851
,0.4708444251
,0.4897720094
,0.4588881757
,0.4509932067
,0.4830097137
,0.4509932067
,0.4509932067
,0.4830097137
,0.4897720094
,0.4588881757
,0.4753091857
,0.4152910209
,0.4753091857
,0.5
,0.3630224959
,0.4152910209
,0.4509932067
,0.4830097137
,0.3489960851
,0.4830097137
,0.4753091857
,0.4588881757
,0.4509932067
,0.4897720094
,0.4830097137
,0.4830097137
,0.4753091857
,0.4897720094
,0.4061625393
,0.4588881757
,0.4897720094
,0.4509932067
,0.4897720094
,0.4830097137
,0.4061625393
,0.3833737441
,0.4830097137
,0.4281561739
,0.4509932067
,0.3630224959
,0.4897720094
,0.4152910209
,0.4897720094
,0.4784376785
,0.5
,0.4897720094
,0.3630224959
,0.3630224959
,0.4830097137
,0.4509932067
,0.3630224959
,0.4453911574
,0.4509932067
,0.3630224959
,0.2683830901
,0.3630224959
,0.4830097137
,0.4830097137
,0.4588881757
,0.4152910209
,0.4830097137
,0.4281561739
,0.4152910209
,0.4281561739
,0.2984533363
,0.4509932067
,0.3630224959
,0.4281561739
,0.4281561739
,0.4830097137
,0.4784376785
,0.4830097137
,0.4152910209
,0.4509932067
,0.4281561739
,0.4281561739
,0.4784376785
,0.4897720094
,0.2491726853
,0.4281561739
,0.4152910209
,0.4509932067
,0.4281561739
,0.4830097137
,0.4509932067
,0.4472006344
,0.4509932067
,0.4830097137
,0.4061625393
,0.3489960851
,0.4897720094
,0.4897720094
,0.4897720094
,0.4152910209
,0.4830097137
,0.4509932067
,0.4061625393
,0.4897720094
,0.4897720094
,0.4830097137
,0.4897720094
,0.4281561739
,0.4588881757
,0.4152910209
,0.4281561739
,0.4588881757
,0.4830097137
,0.4472006344
,0.4281561739
,0.4281561739
,0.4830097137
,0.4897720094
,0.4588881757
,0.4281561739
,0.3630224959
,0.4281561739
,0.3630224959
,0.4830097137
,0.4509932067
,0.4509932067
,0.3630224959
,0.4703770115
,0.4152910209
,0.4897720094
,0.4509932067
,0.4588881757
,0.4784376785
,0.4509932067
,0.4152910209
,0.5
,0.4830097137
,0.4588881757
,0.4509932067
,0.4897720094
,0.4897720094
,0.4830097137
,0.4830097137
,0.4588881757
,0.4588881757
,0.4784376785
,0.4509932067
,0.4453911574
,0.4830097137
,0.4509932067
,0.4784376785
,0.4784376785
,0.4703770115
,0.4784376785
,0.3630224959
,0.4784376785
,0.4830097137
,0.4588881757
,0.4509932067
,0.3630224959
,0.4472006344
,0.4152910209
,0.4703770115
,0.3833737441
,0.4152910209
,0.4897720094
,0.4588881757
,0.3630224959
,0.3630224959
,0.4061625393
,0.4897720094
,0.4509932067
,0.3630224959
,0.2683830901
,0.4588881757
,0.4830097137
,0.4830097137
,0.4588881757
,0.4281561739
,0.4703770115
,0.4152910209
,0.4509932067
,0.4152910209
,0.4897720094
,0.4152910209
,0.4830097137
,0.4897720094
,0.3489960851
,0.4703770115
,0.4830097137
,0.4588881757
,0.4784376785
,0.3630224959
,0.4753091857
,0.3833737441
,0.4061625393
,0.4897720094
,0.4703770115
,0.4061625393
,0.4897720094
,0.4152910209
,0.4509932067
,0.4897720094
,0.4509932067
,0.4061625393
,0.4588881757
,0.4784376785
,0.4830097137
,0.4830097137
,0.3630224959
,0.4830097137
,0.3630224959
,0.2683830901
,0.4061625393
,0.3489960851
,0.3489960851
,0.3833737441
,0.3833737441
,0.3630224959
,0.4588881757
,0.4152910209
,0.4281561739
,0.4703770115
,0.4830097137
,0.4897720094
,0.4152910209
,0.4152910209
,0.4281561739
,0.4152910209
,0.4061625393
,0.4281561739
,0.4151735045
,0.4453911574
,0.4281561739
,0.4897720094
,0.4897720094
,0.4830097137
,0.3630224959
,0.4784376785
,0.4897720094
,0.4708444251
,0.4152910209
,0.4152910209
,0.3630224959
,0.4509932067
,0.4453911574
,0.4061625393
,0.5
,0.5
,0.3833737441
,0.3833737441
,0.4588881757
,0.4588881757
,0.4281561739
,0.3630224959
,0.4830097137
,0.4152910209
,0.4703770115
,0.4152910209
,0.4830097137
,0.3630224959
,0.4784376785
,0.3630224959
,0.2491726853
,0.4753091857
,0.2683830901
,0.4830097137
,0.4830097137
,0.4061625393
,0.4509932067
,0.4281561739
,0.4453911574
,0.4152910209
,0.4061625393
,0.2491726853
,0.4453911574
,0.3489960851
,0.4281561739
,0.4152910209
,0.4152910209
,0.4784376785
,0.4281561739
,0.3833737441
,0.5
,0.4703770115
,0.4588881757
,0.4703770115
,0.3630224959
,0.4281561739
,0.5
,0.4151735045
,0.3630224959
,0.4588881757
,0.4281561739
,0.4897720094
,0.3630224959
,0.4061625393
,0.4897720094
,0.3630224959
,0.4830097137
,0.3630224959
,0.4830097137
,0.4588881757
,0.4061625393
,0.4753091857
,0.4061625393
,0.3630224959
,0.4774017371
,0.4784376785
,0.4830097137
,0.4509932067
,0.4784376785
,0.2683830901
,0.4897720094
,0.3833737441
,0.3833737441
,0.4897720094
,0.4830097137
,0.4784376785
,0.4830097137
,0.4509932067
,0.3489960851
,0.4509932067
,0.4830097137
,0.4151735045
,0.3630224959
,0.4753091857
,0.4509932067
,0.4897720094
,0.4830097137
,0.4830097137
,0.4588881757
,0.4830097137
,0.4830097137
,0.4509932067
,0.3630224959
,0.4784376785
,0.4588881757
,0.4151735045
,0.4281561739
,0.2491726853
,0.4784376785
,0.4509932067
,0.2683830901
,0.4061625393
,0.4152910209
,0.3630224959
,0.4152910209
,0.4753091857
,0.4784376785
,0.4897720094
,0.4784376785
,0.4509932067
,0.4509932067
,0.4152910209
,0.4897720094
,0.4703770115
,0.4152910209
,0.4897720094
,0.3833737441
,0.4703770115
,0.4588881757
,0.4830097137
,0.4152910209
,0.4830097137
,0.4897720094
,0.4897720094
,0.4703770115
,0.4472006344
,0.4703770115
,0.4784376785
,0.4588881757
,0.4509932067
,0.4588881757
,0.4152910209
,0.4588881757
,0.4830097137
,0.4509932067
,0.4784376785
,0.4281561739
,0.4703770115
,0.4784376785
,0.4703770115
,0.4830097137
,0.4897720094
,0.4784376785
,0.4897720094
,0.4703770115
,0.4152910209
,0.4588881757
,0.4509932067
,0.4703770115
,0.5
,0.4588881757
,0.4281561739
,0.4784376785
,0.3833737441
,0.4784376785
,0.4509932067
,0.4830097137
,0.4588881757
,0.4588881757
,0.4509932067
,0.3630224959
,0.4830097137
,0.4061625393
,0.4588881757
,0.4897720094
,0.4830097137
,0.4784376785
,0.4897720094
,0.4588881757
,0.4830097137
,0.4784376785
,0.4897720094
,0.4152910209
,0.4588881757
,0.4281561739
,0.4061625393
,0.4152910209
,0.4061625393
,0.4703770115
,0.4453911574
,0.4453911574
,0.4509932067
,0.4152910209
,0.4509932067
,0.4281561739
,0.4588881757
,0.4509932067
,0.4897720094
,0.4152910209
,0.4897720094
,0.4830097137
,0.4830097137
,0.4784376785
,0.4897720094
,0.4152910209
,0.4830097137
,0.4830097137
,0.4830097137
,0.4830097137
,0.4897720094
,0.4784376785
,0.4784376785
,0.4753091857
,0.4281561739
,0.4784376785
,0.4281561739
,0.4784376785
,0.4472006344
,0.3833737441
,0.4703770115
,0.2491726853
,0.4703770115
,0.4703770115
,0.4753091857
,0.4152910209
,0.4281561739
,0.4061625393
,0.4588881757
,0.4588881757
,0.4830097137
,0.4897720094
,0.4152910209
,0.4784376785
,0.3630224959
,0.4830097137
,0.4784376785
,0.4509932067
,0.4784376785
,0.4588881757
,0.4281561739
,0.4453911574
,0.4152910209
,0.4897720094
,0.4472006344
,0.4281561739
,0.4472006344
,0.4703770115
,0.4708444251
,0.4784376785
,0.4281561739
,0.4152910209
,0.4453911574
,0.4152910209
,0.4281561739
,0.4509932067
,0.4830097137
,0.4897720094
,0.4703770115
,0.4897720094
,0.4588881757
,0.4784376785
,0.4784376785
,0.5
,0.4588881757
,0.4897720094
,0.4509932067
,0.4152910209
,0.4897720094
,0.4784376785
,0.2984533363
,0.4061625393
,0.4509932067
,0.4830097137
,0.3630224959
,0.4152910209
,0.4784376785
,0.4897720094
,0.4703770115
,0.4472006344
,0.2491726853
,0.4784376785
,0.4509932067
,0.4152910209
,0.4152910209
,0.4061625393
,0.3489960851
,0.4897720094
,0.4897720094
,0.4830097137
,0.4897720094
,0.2491726853
,0.4588881757
,0.4152910209
,0.4061625393
,0.4588881757
,0.3833737441
,0.4281561739
,0.4588881757
,0.4703770115
,0.4784376785
,0.4753091857
,0.4281561739
,0.3833737441
,0.4588881757
,0.4830097137
,0.4152910209
,0.3630224959
,0.4509932067
,0.4152910209
,0.3630224959
,0.2683830901
,0.4588881757
,0.3630224959
,0.4281561739
,0.4784376785
,0.4830097137
,0.4152910209
,0.4830097137
,0.4588881757
,0.4897720094
,0.4830097137
,0.4588881757
,0.4784376785
,0.5
,0.4703770115
,0.4281561739
,0.4830097137
,0.4830097137
,0.4784376785
,0.4897720094
,0.4897720094
,0.4897720094
,0.4703770115
,0.4588881757
,0.487845443
,0.4897720094
,0.4509932067
,0.4509932067
,0.4472006344
,0.2984533363
,0.4453911574
,0.4281561739
,0.4509932067
,0.3630224959
,0.3833737441
,0.3630224959
,0.3630224959
,0.2683830901
,0.2984533363
,0.4061625393
,0.4588881757
,0.4453911574
,0.4897720094
,0.4152910209
,0.4703770115
,0.3630224959
,0.4588881757
,0.4784376785
,0.3833737441
,0.4281561739
,0.3833737441
,0.4830097137
,0.4830097137
,0.4784376785
,0.4588881757
,0.4281561739
,0.4472006344
,0.4509932067
,0.4897720094
,0.4472006344
,0.487845443
,0.4453911574
,0.4152910209
,0.4509932067
,0.2984533363
,0.4830097137
,0.4588881757
,0.4453911574
,0.4588881757
,0.5
,0.4152910209
,0.2984533363
,0.4784376785
,0.4509932067
,0.4152910209
,0.3489960851
,0.4897720094
,0.3833737441
,0.4703770115
,0.4281561739
,0.4509932067
,0.4703770115
,0.4281561739
,0.4061625393
,0.3630224959
,0.4588881757
,0.3630224959
,0.4152910209
,0.4152910209
,0.4830097137
,0.4897720094
,0.4897720094
,0.4509932067
,0.4588881757
,0.4509932067
,0.4830097137
,0.4784376785
,0.3630224959
,0.4152910209
,0.4061625393
,0.4784376785
,0.4588881757
,0.4897720094
,0.4281561739
,0.4281561739
,0.3630224959]
precision_diff = [-0.02485629761,
-0.02485629761,
0.5000919512,
0.5000919512,
0.2445958282,
0.2445958282,
-0.0248850469,
-0.02485629761,
0.5000919512,
0.5001226091,
-0.02485629761,
0.500061297,
0.500061297,
0.5000919512,
0.2445958282,
0.500061297,
0.2445352623,
0.5000306466,
0.2445655432,
0.2445049856,
0.5000919512,
0.2445655432,
0.5000919512,
0.2445655432,
0.2445352623,
0.500061297,
0.5000919512,
0.500061297,
0.500061297,
0.500061297,
0.5000306466,
0.500061297,
0.2445049856,
0.500061297,
0.2445655432,
0.500061297,
0.2445655432,
0.5000306466,
0.5000306466,
0.5000306466,
0.5000306466,
0.5000306466,
-0.3141104939,
-0.0248850469,
0.2445049856,
-0.0248850469,
-0.0248850469,
-0.3141605788,
0.2445352623,
0.5000306466,
-0.3141856147,
-0.3141605788,
0.2445049856,
0.500061297,
0.2445352623,
0.2445049856,
0.5000919512,
-0.3141355386,
-0.02482754392,
-0.3141605788,
-0.633197023,
-0.0248850469,
0.5000919512,
0.2445352623,
-0.02485629761,
-0.02485629761,
0.2445655432,
0.2445352623,
0.5000919512,
0.2445352623,
0.5001226091,
0.5000306466,
0.2445655432,
0.500061297,
0.5,
0.2445352623,
0.5000306466,
0.500061297,
0.2445352623,
-0.02485629761,
0.2445655432,
0.5000306466,
0.2445352623,
0.500061297,
-0.3141104939,
0.2445352623,
0.5000919512,
-0.0248850469,
-0.02482754392,
0.2445958282,
-0.02482754392,
0.2445049856,
-0.3141605788,
-0.0248850469,
0.2445352623,
0.500061297,
0.2445049856,
0.5,
0.5000919512,
0.5000306466,
0.5001226091,
0.2445958282,
0.500061297,
0.500061297,
0.500061297,
0.2445655432,
0.5000919512,
0.2445049856,
-0.0248850469,
0.2445352623,
0.5000919512,
-0.02491379178,
0.2445352623,
-0.3141605788,
0.2445049856,
0.2445049856,
0.500061297,
0.5000919512,
0.5000306466,
-0.02485629761,
0.5000306466,
0.2445049856,
0.2444747129,
0.5000919512,
-0.02485629761,
0.500061297,
-0.0248850469,
-0.0248850469,
-0.3141355386,
-0.3141355386,
0.5000306466,
0.2445958282,
0.2445049856,
0.5000919512,
0.2445049856,
0.2445049856,
0.5000919512,
0.5000306466,
0.2445352623,
0.5000306466,
0.500061297,
-0.3141104939,
-0.02485629761,
0.500061297,
0.2445655432,
0.500061297,
0.5000306466,
0.500061297,
0.2445655432,
-0.0248850469,
0.2445049856,
-0.3141355386,
0.500061297,
-0.633214074,
0.2445655432,
-0.0248850469,
-0.3141104939,
-0.3142106462,
0.5000306466,
0.2445352623,
0.2445655432,
0.500061297,
0.2445655432,
0.2445655432,
0.500061297,
0.5000306466,
0.2445352623,
0.5001226091,
-0.02485629761,
0.5001226091,
0.5,
-0.3141355386,
-0.02485629761,
0.2445655432,
0.500061297,
-0.3141104939,
0.500061297,
0.5001226091,
0.2445352623,
0.2445655432,
0.5000306466,
0.500061297,
0.500061297,
0.5001226091,
0.5000306466,
-0.02482754392,
0.2445352623,
0.5000306466,
0.2445655432,
0.5000306466,
0.500061297,
-0.02482754392,
-0.3141605788,
0.500061297,
-0.0248850469,
0.2445655432,
-0.3141355386,
0.5000306466,
-0.02485629761,
0.5000306466,
0.5000919512,
0.5,
0.5000306466,
-0.3141355386,
-0.3141355386,
0.500061297,
0.2445655432,
-0.3141355386,
0.2445958282,
0.2445655432,
-0.3141355386,
-0.633214074,
-0.3141355386,
0.500061297,
0.500061297,
0.2445352623,
-0.02485629761,
0.500061297,
-0.0248850469,
-0.02485629761,
-0.0248850469,
-0.6332311215,
0.2445655432,
-0.3141355386,
-0.0248850469,
-0.0248850469,
0.500061297,
0.5000919512,
0.500061297,
-0.02485629761,
0.2445655432,
-0.0248850469,
-0.0248850469,
0.5000919512,
0.5000306466,
-0.633197023,
-0.0248850469,
-0.02485629761,
0.2445655432,
-0.0248850469,
0.500061297,
0.2445655432,
-0.02491379178,
0.2445655432,
0.500061297,
-0.02482754392,
-0.3141104939,
0.5000306466,
0.5000306466,
0.5000306466,
-0.02485629761,
0.500061297,
0.2445655432,
-0.02482754392,
0.5000306466,
0.5000306466,
0.500061297,
0.5000306466,
-0.0248850469,
0.2445352623,
-0.02485629761,
-0.0248850469,
0.2445352623,
0.500061297,
-0.02491379178,
-0.0248850469,
-0.0248850469,
0.500061297,
0.5000306466,
0.2445352623,
-0.0248850469,
-0.3141355386,
-0.0248850469,
-0.3141355386,
0.500061297,
0.2445655432,
0.2445655432,
-0.3141355386,
0.2445049856,
-0.02485629761,
0.5000306466,
0.2445655432,
0.2445352623,
0.5000919512,
0.2445655432,
-0.02485629761,
0.5,
0.500061297,
0.2445352623,
0.2445655432,
0.5000306466,
0.5000306466,
0.500061297,
0.500061297,
0.2445352623,
0.2445352623,
0.5000919512,
0.2445655432,
0.2445958282,
0.500061297,
0.2445655432,
0.5000919512,
0.5000919512,
0.2445049856,
0.5000919512,
-0.3141355386,
0.5000919512,
0.500061297,
0.2445352623,
0.2445655432,
-0.3141355386,
-0.02491379178,
-0.02485629761,
0.2445049856,
-0.3141605788,
-0.02485629761,
0.5000306466,
0.2445352623,
-0.3141355386,
-0.3141355386,
-0.02482754392,
0.5000306466,
0.2445655432,
-0.3141355386,
-0.633214074,
0.2445352623,
0.500061297,
0.500061297,
0.2445352623,
-0.0248850469,
0.2445049856,
-0.02485629761,
0.2445655432,
-0.02485629761,
0.5000306466,
-0.02485629761,
0.500061297,
0.5000306466,
-0.3141104939,
0.2445049856,
0.500061297,
0.2445352623,
0.5000919512,
-0.3141355386,
0.5001226091,
-0.3141605788,
-0.02482754392,
0.5000306466,
0.2445049856,
-0.02482754392,
0.5000306466,
-0.02485629761,
0.2445655432,
0.5000306466,
0.2445655432,
-0.02482754392,
0.2445352623,
0.5000919512,
0.500061297,
0.500061297,
-0.3141355386,
0.500061297,
-0.3141355386,
-0.633214074,
-0.02482754392,
-0.3141104939,
-0.3141104939,
-0.3141605788,
-0.3141605788,
-0.3141355386,
0.2445352623,
-0.02485629761,
-0.0248850469,
0.2445049856,
0.500061297,
0.5000306466,
-0.02485629761,
-0.02485629761,
-0.0248850469,
-0.02485629761,
-0.02482754392,
-0.0248850469,
-0.3141856147,
0.2445958282,
-0.0248850469,
0.5000306466,
0.5000306466,
0.500061297,
-0.3141355386,
0.5000919512,
0.5000306466,
-0.3142106462,
-0.02485629761,
-0.02485629761,
-0.3141355386,
0.2445655432,
0.2445958282,
-0.02482754392,
0.5,
0.5,
-0.3141605788,
-0.3141605788,
0.2445352623,
0.2445352623,
-0.0248850469,
-0.3141355386,
0.500061297,
-0.02485629761,
0.2445049856,
-0.02485629761,
0.500061297,
-0.3141355386,
0.5000919512,
-0.3141355386,
-0.633197023,
0.5001226091,
-0.633214074,
0.500061297,
0.500061297,
-0.02482754392,
0.2445655432,
-0.0248850469,
0.2445958282,
-0.02485629761,
-0.02482754392,
-0.633197023,
0.2445958282,
-0.3141104939,
-0.0248850469,
-0.02485629761,
-0.02485629761,
0.5000919512,
-0.0248850469,
-0.3141605788,
0.5,
0.2445049856,
0.2445352623,
0.2445049856,
-0.3141355386,
-0.0248850469,
0.5,
-0.3141856147,
-0.3141355386,
0.2445352623,
-0.0248850469,
0.5000306466,
-0.3141355386,
-0.02482754392,
0.5000306466,
-0.3141355386,
0.500061297,
-0.3141355386,
0.500061297,
0.2445352623,
-0.02482754392,
0.5001226091,
-0.02482754392,
-0.3141355386,
-0.02494253226,
0.5000919512,
0.500061297,
0.2445655432,
0.5000919512,
-0.633214074,
0.5000306466,
-0.3141605788,
-0.3141605788,
0.5000306466,
0.500061297,
0.5000919512,
0.500061297,
0.2445655432,
-0.3141104939,
0.2445655432,
0.500061297,
-0.3141856147,
-0.3141355386,
0.5001226091,
0.2445655432,
0.5000306466,
0.500061297,
0.500061297,
0.2445352623,
0.500061297,
0.500061297,
0.2445655432,
-0.3141355386,
0.5000919512,
0.2445352623,
-0.3141856147,
-0.0248850469,
-0.633197023,
0.5000919512,
0.2445655432,
-0.633214074,
-0.02482754392,
-0.02485629761,
-0.3141355386,
-0.02485629761,
0.5001226091,
0.5000919512,
0.5000306466,
0.5000919512,
0.2445655432,
0.2445655432,
-0.02485629761,
0.5000306466,
0.2445049856,
-0.02485629761,
0.5000306466,
-0.3141605788,
0.2445049856,
0.2445352623,
0.500061297,
-0.02485629761,
0.500061297,
0.5000306466,
0.5000306466,
0.2445049856,
-0.02491379178,
0.2445049856,
0.5000919512,
0.2445352623,
0.2445655432,
0.2445352623,
-0.02485629761,
0.2445352623,
0.500061297,
0.2445655432,
0.5000919512,
-0.0248850469,
0.2445049856,
0.5000919512,
0.2445049856,
0.500061297,
0.5000306466,
0.5000919512,
0.5000306466,
0.2445049856,
-0.02485629761,
0.2445352623,
0.2445655432,
0.2445049856,
0.5,
0.2445352623,
-0.0248850469,
0.5000919512,
-0.3141605788,
0.5000919512,
0.2445655432,
0.500061297,
0.2445352623,
0.2445352623,
0.2445655432,
-0.3141355386,
0.500061297,
-0.02482754392,
0.2445352623,
0.5000306466,
0.500061297,
0.5000919512,
0.5000306466,
0.2445352623,
0.500061297,
0.5000919512,
0.5000306466,
-0.02485629761,
0.2445352623,
-0.0248850469,
-0.02482754392,
-0.02485629761,
-0.02482754392,
0.2445049856,
0.2445958282,
0.2445958282,
0.2445655432,
-0.02485629761,
0.2445655432,
-0.0248850469,
0.2445352623,
0.2445655432,
0.5000306466,
-0.02485629761,
0.5000306466,
0.500061297,
0.500061297,
0.5000919512,
0.5000306466,
-0.02485629761,
0.500061297,
0.500061297,
0.500061297,
0.500061297,
0.5000306466,
0.5000919512,
0.5000919512,
0.5001226091,
-0.0248850469,
0.5000919512,
-0.0248850469,
0.5000919512,
-0.02491379178,
-0.3141605788,
0.2445049856,
-0.633197023,
0.2445049856,
0.2445049856,
0.5001226091,
-0.02485629761,
-0.0248850469,
-0.02482754392,
0.2445352623,
0.2445352623,
0.500061297,
0.5000306466,
-0.02485629761,
0.5000919512,
-0.3141355386,
0.500061297,
0.5000919512,
0.2445655432,
0.5000919512,
0.2445352623,
-0.0248850469,
0.2445958282,
-0.02485629761,
0.5000306466,
-0.02491379178,
-0.0248850469,
-0.02491379178,
0.2445049856,
-0.3142106462,
0.5000919512,
-0.0248850469,
-0.02485629761,
0.2445958282,
-0.02485629761,
-0.0248850469,
0.2445655432,
0.500061297,
0.5000306466,
0.2445049856,
0.5000306466,
0.2445352623,
0.5000919512,
0.5000919512,
0.5,
0.2445352623,
0.5000306466,
0.2445655432,
-0.02485629761,
0.5000306466,
0.5000919512,
-0.6332311215,
-0.02482754392,
0.2445655432,
0.500061297,
-0.3141355386,
-0.02485629761,
0.5000919512,
0.5000306466,
0.2445049856,
-0.02491379178,
-0.633197023,
0.5000919512,
0.2445655432,
-0.02485629761,
-0.02485629761,
-0.02482754392,
-0.3141104939,
0.5000306466,
0.5000306466,
0.500061297,
0.5000306466,
-0.633197023,
0.2445352623,
-0.02485629761,
-0.02482754392,
0.2445352623,
-0.3141605788,
-0.0248850469,
0.2445352623,
0.2445049856,
0.5000919512,
0.5001226091,
-0.0248850469,
-0.3141605788,
0.2445352623,
0.500061297,
-0.02485629761,
-0.3141355386,
0.2445655432,
-0.02485629761,
-0.3141355386,
-0.633214074,
0.2445352623,
-0.3141355386,
-0.0248850469,
0.5000919512,
0.500061297,
-0.02485629761,
0.500061297,
0.2445352623,
0.5000306466,
0.500061297,
0.2445352623,
0.5000919512,
0.5,
0.2445049856,
-0.0248850469,
0.500061297,
0.500061297,
0.5000919512,
0.5000306466,
0.5000306466,
0.5000306466,
0.2445049856,
0.2445352623,
0.2444747129,
0.5000306466,
0.2445655432,
0.2445655432,
-0.02491379178,
-0.6332311215,
0.2445958282,
-0.0248850469,
0.2445655432,
-0.3141355386,
-0.3141605788,
-0.3141355386,
-0.3141355386,
-0.633214074,
-0.6332311215,
-0.02482754392,
0.2445352623,
0.2445958282,
0.5000306466,
-0.02485629761,
0.2445049856,
-0.3141355386,
0.2445352623,
0.5000919512,
-0.3141605788,
-0.0248850469,
-0.3141605788,
0.500061297,
0.500061297,
0.5000919512,
0.2445352623,
-0.0248850469,
-0.02491379178,
0.2445655432,
0.5000306466,
-0.02491379178,
0.2444747129,
0.2445958282,
-0.02485629761,
0.2445655432,
-0.6332311215,
0.500061297,
0.2445352623,
0.2445958282,
0.2445352623,
0.5,
-0.02485629761,
-0.6332311215,
0.5000919512,
0.2445655432,
-0.02485629761,
-0.3141104939,
0.5000306466,
-0.3141605788,
0.2445049856,
-0.0248850469,
0.2445655432,
0.2445049856,
-0.0248850469,
-0.02482754392,
-0.3141355386,
0.2445352623,
-0.3141355386,
-0.02485629761,
-0.02485629761,
0.500061297,
0.5000306466,
0.5000306466,
0.2445655432,
0.2445352623,
0.2445655432,
0.500061297,
0.5000919512,
-0.3141355386,
-0.02485629761,
-0.02482754392,
0.5000919512,
0.2445352623,
0.5000306466,
-0.0248850469,
-0.0248850469,
-0.3141355386]

# Perform the Wilcoxon signed-rank test
res = wilcoxon(accuracy_diff)

print(res.statistic)
print(res.pvalue)