// Konfirmasi sebelum hapus reminder
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-delete');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Yakin ingin menghapus reminder ini?')) {
                e.preventDefault();
            }
        });
    });
});