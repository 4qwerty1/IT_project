<template>
  <div class="home">
    <div>
      <input type="text" id="name" maxlength="15" placeholder="Имя">
    </div>

    <div style="margin-top: 10px">
      <input type="text" id="surname" maxlength="20" placeholder="Фамилия">
    </div>

    <div>
      <ul style="list-style: none; padding-left: 15px">
        <li style="display: inline; padding-right: 20px"><input name="sex" type="radio">Муж</li>
        <li style="display: inline; padding-right: 20px"><input name="sex" type="radio">Жен</li>
      </ul>
    </div>

    <div>
      <select>
        <option>Любимый ЯП</option>
        <option>C</option>
        <option>C++</option>
        <option>C++++ (aka C#)</option>
        <option>Python</option>
        <option>Java</option>
        <option>Я гуманитарий</option>
      </select>
    </div>

    <div style="margin: 10px">
      <select>
        <option>Любимый pattern</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>Я гуманитарий</option>
      </select>
    </div>
  </div>

</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';

@Options({
  components: {}
})
export default class Home extends Vue {
}
</script>
