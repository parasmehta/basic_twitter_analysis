register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

mytriples = filter ntriples by (subject matches '.*business.*');

mytriples2 = foreach mytriples generate $0 as subject2,$1 as predicate2,$2 as object2;

commontriples = join mytriples by (subject), mytriples2 by (subject2);

distincttriples = distinct commontriples;

store distincttriples into '/tmp/threeoutputdistinct' using PigStorage();
