function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// navigation
const navmenubtn = document.querySelector(".nav-menu-btn");
const navmenubtnicon = document.querySelectorAll(".nav-menu-btn-icon");
const navmenu = document.querySelector(".nav-menu");

if (navmenubtn) {
  navmenubtn.addEventListener("click", () => {
    navmenubtnicon.forEach(element => {
      element.classList.toggle('hidden')
    });
    navmenu.classList.toggle("hidden");
    navmenubtn.lastElementChild.textContent == 'menu button' ? navmenubtn.lastElementChild.textContent = 'close menu' : navmenubtn.lastElementChild.textContent = 'menu button'
  });
}

const usermenudropdown = document.querySelector('.user-menu-dropdown')
const usermenudropdownbutton = document.querySelector('.user-menu-dropdown-button')

if (usermenudropdownbutton) {
  usermenudropdownbutton.addEventListener('click', () => {
    usermenudropdown.classList.toggle("hidden")
  })
}

// search

const search = document.querySelector(".search");
const searchbutton = document.querySelectorAll(".searchbutton");

if (searchbutton) {
  searchbutton.forEach((searchbutton) => {
    searchbutton.addEventListener("click", () => {
      search.classList.toggle("flex");
      search.classList.toggle("hidden");
    })
  })
}

if (search) {
  search.addEventListener("click", (e) => {
    if (e.target.matches('.search') || !e.target.closest('input')) {
      search.classList.toggle("flex");
      search.classList.toggle("hidden");
    }
  })
}

window.onkeydown = (e) => {
  searckkey(e)
}

function searckkey(e) {
  if (e.ctrlKey && e.key == 'k' || e.key == 'K') {
    e.preventDefault()
    search.classList.add("flex");
    search.classList.remove("hidden");
  }
  if (e.key == 'Escape') {
    e.preventDefault()
    search.classList.remove("flex");
    search.classList.add("hidden");
  }
}

//  darkmode

const darkmodebuttons = document.querySelectorAll('.darkmodebutton')
const sun = document.querySelectorAll('.sun')
const moon = document.querySelectorAll('.moon')

darkmodebuttons.forEach(darkmodebutton => {
  darkmodebutton.addEventListener('click', darkmode)
})

function darkmode() {
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.remove('dark')
    localStorage.theme = 'light'
  } else {
    document.documentElement.classList.add('dark')
    localStorage.theme = 'dark'
  }
  sun.forEach(sun => {
    sun.classList.toggle('hidden')
  })
  moon.forEach(moon => {
    moon.classList.toggle('hidden')
  })
}

function toggleReplyForm(commentId) {
  const form = document.getElementById(`reply-form-${commentId}`);
  form.classList.toggle('hidden');
  if (!form.classList.contains('hidden')) {
    const textarea = form.querySelector('textarea');
    textarea?.focus();
  }
}

function toggleReplies(commentId) {
  const repliesDiv = document.getElementById(`replies-${commentId}`);
  const btn = document.getElementById(`toggle-replies-btn-${commentId}`);

  if (repliesDiv.classList.contains('hidden')) {
    repliesDiv.classList.remove('hidden');
    btn.textContent = 'Hide Replies';
  } else {
    repliesDiv.classList.add('hidden');
    btn.textContent = `Show Replies (${repliesDiv.children.length})`;
  }
}

// Notifications

const notifications = document.querySelectorAll('.notifications')

if (notifications) {
  notifications.forEach(notification => {
    notificationclosebutton = notification.querySelector('.notification-close-button')
    notificationinterval = setTimeout(() => {
      notification.classList.add('opacity-0', 'translate-x-full')
      clearTimeout(notificationclosebutton)
    }, 6000)
    notificationclosebutton.addEventListener('click', () => {
      notification.classList.add('opacity-0', 'translate-x-full')
      notification.addEventListener('transitionend', () => {
        notification.remove()
      })
    })
  })
}

// footer year
const footeryear = document.querySelector('.footer-year')

yeardate = new Date()

footeryear.textContent = yeardate.getFullYear()

const subscribeform = document.querySelector('.subscribeform')
const subscribeformbutton = document.querySelector('.subscribeformbutton')

if (subscribeform) {

  subscribeform.addEventListener('submit', (e) => {
    e.preventDefault()
    const subscribemessage = document.querySelector('.subscribemessage')
    const subscribedefault = document.querySelector('.subscribedefault')
    const subscribesending = document.querySelector('.subscribesending')
    const subscribedone = document.querySelector('.subscribedone')

    subscribeformbutton.disabled = true
    subscribedefault.classList.toggle('hidden')
    subscribesending.classList.toggle('hidden')

    const subscribeformdata = new FormData(e.target)
    email = { 'email': subscribeformdata.get('email'), 'name': subscribeformdata.get('name') }
    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
      // mode: 'same-origin',
      body: JSON.stringify(email)
    };

    fetch('/subscribe/', options)
      .then(response => {
        if (!response.ok) {
          throw new error('There was a problem')
        }
        if (response.ok) {
          subscribesending.classList.toggle('hidden')
          subscribedone.classList.toggle('hidden')
          setTimeout(() => {
            subscribeformbutton.disabled = false
            subscribedefault.classList.toggle('hidden')
            subscribedone.classList.toggle('hidden')
          }, 1000)
        }
        return response.json()
      })
      .then(response => {
        console.log(response)
        if (response.created == false) {
          subscribemessage.textContent = 'This Email Already Subscribed'
        }
        setTimeout(() => {
          subscribemessage.textContent = ''
        }, 2000)
      }
      )
      .catch(err => console.error(err));
  })
}