var add_item_field = function() {
  var item = '<div class = "item"><input type="text" class="form-control" placeholder="Item Description"><div class="form-group item-questions"><input type="text" class="form-control item-question" placeholder="Question"></div><button type="button" class="btn btn-primary add-question">Add Question</button></div>';
  $('.form-items').append(item);
  };

var add_question_field = function() {
      var question = '<input type="text" class="form-control item-question" placeholder="Question">'
      clicked.prev().append(question);
};

var main = function() {
  $('.add-item').click(add_item_field());
}

$(document).ready(main());
