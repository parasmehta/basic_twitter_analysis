register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

countsgroup = group ntriples by (subject);

count_by_subject = foreach countsgroup generate flatten($0), COUNT($1) as count;

subjectsgroup = group count_by_subject by (count);

subjects_by_count = foreach subjectsgroup generate flatten($0), COUNT($1) as subjectcount;

store subjects_by_count into '/user/hadoop/twobresults' using PigStorage();


