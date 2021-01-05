<template>
  <div>
    <md-content class="md-scrollbar">
      <div class="msg-container" v-for="message in messages" :key="message.id">
        <div class="left">
          <md-avatar>
            <img :src="'http://localhost:8000' + message.get_avatar" alt="Ava">
          </md-avatar>
          <span class="name">{{ message.get_name }}</span>
        </div>
        <div class="message">{{ message.text }}</div>
      </div>
    </md-content>
  </div>
</template>

<script lang="js">
export default {
  name: "ChatView",
  props: {
    messages: {
      required: true,
      type: Array,
      default: () => [{
        id: 0,            // message id
        // eslint-disable-next-line @typescript-eslint/camelcase
        get_name: 'name',// sender name
        // eslint-disable-next-line @typescript-eslint/camelcase
        get_avatar: 'url',      // icon url
        text: 'message'   // message text
      }]
    }
  }
}
// TODO Размер имени
// TODO Выводить логин, если нет имени
// TODO Доделать профиль
// TODO Написать запросы
// TODO Научиться отправлять фото

</script>

<style lang="scss" scoped>

.md-content {
  height: 70ex;
  overflow: auto;
}

.msg-container {
  position: relative;
  min-height: 50px;
}

.left {
  position: absolute;
  display: block;

  left: 10px;
  top: 6px;

  z-index: 2;
  text-align: left;
}

.name {
  position: absolute;
  padding-left: 5px;
  font-size: 12.5px;
  font-weight: 600; // TEST 600-700
}

.message {
  display: block;
  text-align: left;

  padding-top: 21px;
  margin-left: 60px;
  margin-right: 40px;
  margin-bottom: 4px;

  font-size: 13px;
  font-weight: 400;
  line-height: 18px;
}

</style>