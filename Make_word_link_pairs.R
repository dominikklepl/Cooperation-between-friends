#load data
data= read.csv("data/data_merged.csv",stringsAsFactors = F)

#we need only columns "link" and "linked"

data = data[,c("link","linked")]

#take subset for testing
test=data[1:3,]

output={}
for (row in 1:nrow(data)) {
  link = data[row,"link"]
  linked = data[row,"linked"]
  
  #split linked into separate words
  linked_split = strsplit(linked,",")
  linked_split=as.data.frame(linked_split)
  
  #2nd column with link word
  link = rep(link,nrow(linked_split))
  
  round_words = cbind(linked_split,link)
  
  #change column names
  colnames(round_words)=c("word","link")
  
  #cbind round_words to the output df
  output=rbind(output,round_words)
}

#unite columns of output into format ready to paste into the questionaire
output[,ncol(output)+1]=tidyr::unite(output,"question_format",sep=" and ")

#randomize the rows
output <- output[sample(1:nrow(output)), ]

write.csv(output,"data/pairs_for_questionaire.csv",row.names = F)

