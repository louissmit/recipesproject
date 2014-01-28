function(doc) {
  if (doc.Ingredients.length !== 0 && doc.Category === 'Desserts') {
      emit(doc._id , {
      	instructions: doc.Instructions,
      	ingredients: doc.Ingredients
      })
  }
}