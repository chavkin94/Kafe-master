function dobavlenie_v_korzinu(tovar_id, kol_vo) {

    let tovari = localStorage.getItem('tovari');
    if (!tovari) {
        tovari = new Map([
            ['', ''],
        ]);
    }

    tovari.set(tovar_id, kol_vo);
    localStorage.setItem('tovari', tovari)
}


$(function () {
    $('.btn_dobavlenie_v_korzinu').click(function (e) {
        e.preventDefault();
        let tovar_id = e.currentTarget.dataset['idBluda'];
        dobavlenie_v_korzinu(tovar_id, 1)
    })
})