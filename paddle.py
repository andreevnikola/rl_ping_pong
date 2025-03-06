import pygame as pg
import sys
import random
import time

class Paddle:
  graphic: pg.Rect
  speed: int
  score: int

  _screen: pg.Surface

  def __init__(self, screen: pg.Surface, x_pos: int, initial_speed: int, initial_score: int) -> pg.Rect:
    self.graphic = pg.Rect(x_pos, screen.get_height() / 2 - 70, 10, 140)
    self.speed = initial_speed
    self.score = initial_score
    self._screen = screen
  
  def increase_score(self):
    self.score += 1

  def reset_score(self):
    self.score = 0

  def accelerate(self, speed: int):
    self.speed += speed

  def move(self):
    self.graphic.y += self.speed
    self._keep_in_bounds()

  def bot_move(self, ball: pg.Rect):
    if ball.y < self.graphic.y:
        self.graphic.y -= self.speed
    if ball.y > self.graphic.y:
        self.graphic.y += self.speed
    self._keep_in_bounds()

  def _keep_in_bounds(self):
    if self.graphic.top <= 0:
        self.graphic.top = 0
    if self.graphic.bottom >= self._screen.get_height():
        self.graphic.bottom = self._screen.get_height()