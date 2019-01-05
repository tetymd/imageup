<template>
    <div id="upload-form">
        <form method="POST" action="http://localhost:8000/api/thread/" target="http://localhost:8080/#/upload">
            <input type="text" name="title"><br>
            <textarea name="description"></textarea>
            <input type="submit" value="送信">
        </form>
    </div>
</template>

