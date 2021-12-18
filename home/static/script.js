const faPattern = /^[\u0600-\u06FF\s]+$/
const faRegex = new RegExp(faPattern)
let currentPrice = price
let couponAmount = 0

function addFields() {
    let count = 1
    const extraFields = document.querySelectorAll('.extra-field')
    if (extraFields.length >= 19) {
        alert("حداکثر تعداد ثبت نام گروهی 20 نفر می باشد")
        return false
    }

   

    const inptus = `
        <div class="extra-field">
            <hr/>
            <p class="round-btn delete" onclick="removeFields(this)">X</p>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">نام</label>
                <input type="text" class="form-control" name="firstname[]" onkeyup="this.parentElement.querySelector('.error').style.display = 'none'" />
                <div class="text-danger error"><small>لطفا نام خود را با حروف فارسی وارد نمایید</small></div>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">نام خانوادگی</label>
                <input type="text" class="form-control" name="lastname[]" onkeyup="this.parentElement.querySelector('.error').style.display = 'none'" />
                <div class="text-danger error"><small>لطفا نام خانوادگی خود را با حروف فارسی وارد نمایید</small></div>
            </div>

            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">ایمیل</label>
                <input id="email" type="email" class="form-control" name="email[]" onkeyup="this.parentElement.querySelector('.error').style.display = 'none'" />
                <div class="text-danger error"><small>لطفا ایمیل خود را وارد نمایید</small></div>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">شماره تلفن همراه</label>
                <input type="number" class="form-control" name="number[]" onkeyup="this.parentElement.querySelector('.error').style.display = 'none'" />
                <div class="text-danger error"><small>لطفا شماره تلفن همراه خود را وارد نمایید</small></div>
            </div>
        </div>
    `

    if (extraFields.length == 0)
        count = 2

    $("#extra-fields").append(inptus.repeat(count))

    document.querySelector("#payment-btn").innerText = 'ثبت‌نام و خرید'
    document.querySelector("#group-btn").innerText = 'افزودن فرد دیگر'

    if (couponAmount == 'free') {
        document.querySelector(".total-price").value = `رایگان`
        return
    }
    currentPrice += (price * count) - (discount * (count == 2 ? 3 : count))
    document.querySelector(".total-price").value = `${currentPrice - couponAmount} تومان`
}

function removeFields(e) {
    let count = 1
    const extraFields = document.querySelector('#extra-fields')
    extraFields.removeChild(e.parentElement)

    if (extraFields.querySelectorAll('.extra-field').length == 1) {
        count = 2
        extraFields.innerHTML = ''
        
    }

    if (!extraFields.querySelector('.extra-field')) {
        document.querySelector("#payment-btn").innerText = 'ثبت نام فردی'
        document.querySelector("#group-btn").innerText = 'ثبت نام گروهی'
    }

    if (couponAmount == 'free') {
        document.querySelector(".total-price").value = `رایگان`
        return
    }
    currentPrice -= (price * count) - (discount * (count == 2 ? 3 : count))
    document.querySelector(".total-price").value = `${currentPrice - couponAmount} تومان`
}

async function check_coupon(e) {
    const email = document.querySelector('.sign-up-section #email').value
    const code = document.querySelector('#coupon').value
    const req = await fetch(`/winter/verify_coupon?code=${code}&email=${email}`)
    const res = await req.text()

    e.parentElement.parentElement.querySelector('.error').style.display = 'none'
    e.parentElement.parentElement.querySelector('.success').style.display = 'none'

    if (req.status === 200) {
        if (res == 'free') {
            couponAmount = res
            document.querySelector(".total-price").value = `رایگان`
        }
        else {
            couponAmount = Number.parseInt(res)

            if ((currentPrice - couponAmount) < 0) {
                document.querySelector(".total-price").value = `${0} تومان`
            } else {
                document.querySelector(".total-price").value = `${currentPrice - couponAmount} تومان`
            }
        }
        e.parentElement.parentElement.querySelector('.success').style.display = 'block'

        return false
    }
    else if (couponAmount != 0) {
        couponAmount = 0
        document.querySelector(".total-price").value = `${currentPrice + couponAmount} تومان`
    }
    e.parentElement.parentElement.querySelector('.error').style.display = 'block'

    return false
}

function on_submit(e) {
    const input_names = ['firstname[]', 'lastname[]', 'email[]', 'number[]']

    for (const n of input_names) {
        const inputs = document.querySelectorAll(`input[name="${n}"]`)

        for (const input of inputs) {
            if (!input.value) {
                input.parentElement.querySelector('.error').style.display = "block"
                return false
            }

            if (input.name == "firstname[]" || input.name == "lastname[]")
                if (!faRegex.test(input.value)) {
                    input.parentElement.querySelector('.error').style.display = "block"
                    return false
                }
        }
    }

    return true
}
