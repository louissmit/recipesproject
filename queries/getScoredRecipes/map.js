function(doc) {
  if (doc.ReviewCount > 5) {
      emit(doc._id , {
      	score: doc.StarRating,
      	fav: doc.FavoriteCount
      })
  }
}