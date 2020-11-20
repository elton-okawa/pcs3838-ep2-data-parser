# Usage
```
python <datasetFileName> <configFileName> <shouldReturnIntervalOutput>
```

# Config file format
The config file must be declared in the same order of dataset columns
```
<name>, <tag>, <intervalSize>
<name>, <tag>, <intervalSize>

Example:
Recency (months), Recency, 1
Frequency (times), Frequency, 5
```

# Output format
If "shouldReturnIntervalOutput" argument is true:
```
<tag>_<inclusiveStartInterval>-<exclusiveEndInterval>, ...

Example:
Recency_0-1, Frequency_10-15, ...
```
Else:
```
<value>, ...

Example:
0, 2, ...
```
