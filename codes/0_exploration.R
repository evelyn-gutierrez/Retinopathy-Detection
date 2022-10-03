library(ggplot2)
library(tidyr)
library(dplyr)

dt <- read.csv(paste0(main_dir,"dataset/train.csv"))

dt_wide <- dt %>% spread(location, level)
cor(dt_wide$left,dt_wide$right, method="spearman")
# 0.8137

dttable <- table(dt_wide$left,dt_wide$right)
dttable
dttable <- data.frame(dttable)
names(dttable)[1:2] <- c("left","right")


dttable %>% filter(left!=0 | right!=0)%>%
ggplot(aes(x=left, y=right, size = Freq, col=Freq)) +
  geom_point(alpha=1) +
  scale_size(range = c(.1, 24), name="Frequency")

# Fuerte dependencia entre el grado de problema de los dos ojos.
