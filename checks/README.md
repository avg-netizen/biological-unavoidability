# Finite diagnostic controls

Both scripts use Python 3's standard library and write JSON beside themselves.

`classification.py` separately transcribes outgoing edges, compares exact
reachable sets against an interval recurrence, checks the path offset, supplies
periodic positive controls, and checks finite-alphabet incoming parents. Its
finite-horizon failures to terminate are reported as unknown, not realizations.

`observation.py` checks finite residue-template paths and lifts, pairs of
indistinguishable initial graph regions, and long finite matches at a fixed
starting vertex. Infinite universality and undecidability are prose proofs.

The scripts are adapted from earlier research scripts, with local output names
and prose references. They have no dependency on the original research notes
or on one another.
