function add_item_field() {
  var item = '<div class = "item"><label for="description">Item</label><input type="text" class="form-control" id="itemID" placeholder="Item Barcode"><input type="text" class="form-control" id="itemType" placeholder="Item Description"><input type="text" class="form-control" id="assignee" placeholder="User Assigned"><div class="form-group item-questions"><label for="question">Item Questions</label><input type="text" class="form-control item-question" placeholder="Question"></div><button type="button" onclick="add_question_field($(this))" class="btn btn-primary add-question">Add Item Question</button></div>';
  $('.form-items').append(item);
  };

function add_question_field(clicked) {
  var question = '<div class="input-group item-input"><input type="text" class="form-control item-question" placeholder="Question"><span class="input-group-btn"><button onclick="remove($(this))" class="btn btn-default" type="button">Remove</button></span></div>'
  clicked.prev().append(question);
};

function add_location_question(clicked) {
  var question = '<div class="input-group loc-question"><input type="text" class="form-control location-question" placeholder="Question"><span class="input-group-btn"><button onclick="remove($(this))" class="btn btn-default" type="button">Remove</button></span></div>'
  clicked.prev().append(question);
};

function remove(clicked) {
  clicked.parent().parent().remove();
};

var main = function() {

};

$(document).ready(main());
