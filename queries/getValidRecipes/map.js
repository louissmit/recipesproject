function(doc) {
  if (doc.Ingredients.length !== 0) {
      emit(doc._id , {
      	instructions: doc.Instructions,
      	ingredients: doc.Ingredients
      })
  }
}