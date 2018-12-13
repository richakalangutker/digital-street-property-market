$(document).ready( function () {
    $('#myTable').DataTable();

    $(".delete_file").click(function(){

        r = confirm("Are you sure?")
        if (r == true) {
            element = this;
           $("#file_loader").show();
           $.ajax({
                      type: "POST",
                      url: "/project/delete/"+this.id,
                      data: {filename:$('#'+this.id).data('file-name')},
                      success: function(){
                           $(element).parent().remove();
                            $("#file_loader").hide();
                      },
                      error:function(request, error) {
                            console.log("error:"+error);
                            $("#file_loader").hide();
                      }
                    });
        } else {
            txt = "You pressed Cancel!";
        }
});
} );