# Set:
# A set object is an unordered collection of distinct hashable objects.
# Common uses include removing duplicates from a sequence and etc.

# Like other collections, sets support x in set, len(set) and
# for x in set. Being an unordered collection, sets do not record
# element position or order of insertion. Accordingly sets do not support
# indexing, slicing or other sequence-like behavior.

# There are currently two built-in set types, set and frozenset.
# The set type is mutable - the contents can be changed using methods like
# add() and remove().
# The frozenset type is immutable and hashable - its contents cannot be
# altered after it is created.

# Two sets are equal if every element of each set is contained in
# the other (each is a subset of the other). A set is less than another set
# if the first set is a proper subset of the second set (is a subset, but not
# equal). A set is greater than another set if and only if the first set is a
# proper superset of the second set (is a superset, but is not equal).

literal_set = {1, 2, 3, 3} # {1, 2, 3}
constructed_set = set([1,2,3])
comprehensive_set = {i for i in [1, 2, 3]}
constructed_frozenset = frozenset([1,2,3])
