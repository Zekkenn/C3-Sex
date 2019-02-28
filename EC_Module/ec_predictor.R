library(tm)
library(SnowballC)
library(caret)
library(tokenizers)
library(dplyr)

# ================================= BAG OF WORDS ===========================================

bag.of.words <- function(data, sparse = 0.999, init = FALSE, test = TRUE){
  docs <- Corpus(VectorSource(data$SIT))
  words.dict <- list()
  if ( init == TRUE ){
    #Remove Sparse Terms
    dtm <- DocumentTermMatrix(docs)
    dtm <- removeSparseTerms(dtm, sparse)
    createDict(dtm)
  } else {
    words.dict <- scan("dict.txt", what = character())
    dtm <- DocumentTermMatrix(docs, list( dictionary = words.dict ))
  }
  
  mat <- as.matrix(dtm)
  data.mat <- as.data.frame(mat)

  return(data.mat)
}


# ================================= PREPROCESS DATA ========================================

preproccess.data <- function(data, stemming = TRUE, language = "english"){
  
  # DELETE ROWS WITH 1 LENGTH SENTENCES
  pos <- which(sapply(tokenize_words(data$SIT), length) %in% c(0,1,2))
  if (length(pos) != 0) {data <- data[-pos,]}
  lg <- ifelse(language=='english',"en",language)
  
  # CLEAN ALL NON-ALPHANUMERIC CHARACTERS & additional whitespace
  data$SIT <- sapply(data$SIT, function(x) gsub("[^a-zA-Z0-9']", " ", x)) # non-alphanumeric characters
  data$SIT <- sapply(data$SIT, function(x) gsub("\\s+", " ", x)) # additional whitespace
  data$SIT <- sapply(data$SIT, function(x) gsub(" $", "", x)) # end Whitespace
  
  
  # TM
  corpus <- Corpus(VectorSource(data$SIT))
  corpus.clean <- corpus %>%
    tm_map(content_transformer(tolower)) %>%
    tm_map(removePunctuation) %>%
    tm_map(removeNumbers) %>%
    tm_map(removeWords, stopwords(kind=lg)) %>%
    tm_map(stripWhitespace)
  
  # GET STEMMING SENTENCES FROM DATA
  if (stemming) {
    str("Stemming Process ...")
    corpus.clean <- tm_map(corpus.clean, PlainTextDocument)  # needs to come before stemming
    corpus.clean <- tm_map(corpus.clean, stemDocument, language)
    data$SIT <- sapply(corpus.clean, identity)$content
  }else{
    data$SIT <- sapply(corpus.clean, identity)
  }
  
  return(data)
}


generateDict <- function(model.trainingdata){
  q2 <- names(model.trainingdata)
  filename <- paste("dict",".txt", sep="")
  writeLines(as.character(q2[-1]), con=filename)
}


# ============================ MORIARTY : USING EC MODULE ==================================

modelEC <- readRDS("models/modelSVM_isear_fin.rds")
#generateDict(modelEC$trainingData)

# READ REPLIES
replies.file <- commandArgs(trailingOnly = TRUE)
replies <- scan(replies.file, what = character(), sep = '\n')

test <- data.frame(SIT = replies, stringsAsFactors = FALSE)
test.rep <- bag.of.words(preproccess.data(test))

predEC <- predict(modelEC, test.rep)

# SAVE PREDICTIONS
filename <- paste("Pred",replies.file, sep="_")
writeLines(as.character(paste(replies,predEC,sep=",")), con=filename)